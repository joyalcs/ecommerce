console.log("hai");
$(".add-to-cart-button").on("click", function(){
    let this_value = $(this);
    let index = this_value.attr("data-index");
    let quantity = $(".product-qty-"+index).val()
    let product_id = $(".product-id-" + index).val();
    let product_name = $(".product-name-" + index).val();
    let product_price = $(".product-price-" + index).val();
    let product_image = $(".product-image-" + index).val();

    $.ajax({
        url: '/add-to-cart/',
        method: 'GET', // Specify the HTTP method explicitly
        data: {
            'id': product_id,
            'name': product_name,
            'qty': quantity,
            'price': product_price,
            'image': product_image,
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("Adding to the Cart");
        },
        success: function(response){
            this_value.html("Added");
            console.log("Item added ");
            $(".cart-item-count").text(response.totalcartitems);
        }
    });
});


$(".delete-product").on("click", function(){
    let this_value = $(this);
    let product_id = $(this).data("product")
    console.log("hai")
    console.log(product_id);

    $.ajax({
        url: '/delete-product-from-cart',
        data: {
            'id': product_id,
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("Deleting")
        },
        success:function(response){
            $(".cart-item-count").text(response.totalcartitems)
            $("#cart-products").html(response.data)
            location.reload();
        }
    });
});

function incrementValue(e) {
    e.preventDefault();
    var fieldName = $(e.target).data('field');
    var parent = $(e.target).closest('div');
    var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

    if (!isNaN(currentVal)) {
        parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
    } else {
        parent.find('input[name=' + fieldName + ']').val(0);
    }
}

function decrementValue(e) {
    e.preventDefault();
    var fieldName = $(e.target).data('field');
    var parent = $(e.target).closest('div');
    var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

    if (!isNaN(currentVal) && currentVal > 0) {
        parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
    } else {
        parent.find('input[name=' + fieldName + ']').val(0);
    }
}

$('.input-group').on('click', '.button-plus', function(e) {
    incrementValue(e);
});

$('.input-group').on('click', '.button-minus', function(e) {
    decrementValue(e);
});
