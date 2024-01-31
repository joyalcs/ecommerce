//Add to cart
console.log("hai");
// $(".add-to-cart-button").on("click", function(){
//     let this_value = $(this)
//     let index = this_value.attr("data-index")
//     let product_id = $(".product-id-"+index).val()
//     let product_name = $(".product-name-"+index).val()
//     let product_price = $(".product-price-"+index).text()
//     let product_image = $(".product-image-"+index).val()
//     console.log(product_price);
//     $.ajax({
//         url:'/add-to-cart/',
//         data:{
//             'id': product_id,
//             'qty': 1,
//             'title': product_name,
//             'price': product_price,
//             'image': product_image,
//         },
//         dataType: 'json',
//         beforeSend:function(){
//             console.log("Adding to the Cart");
//         },
//         success:function(response){
//             this_value.html("Added")
//             console.log("Item added ")
//             $(".cart-item-count").text(response.totalcartitems)
//         }
//     })
// });

// Delete the cart item


// $(".delete-product").on("click", function(){
//     let this_value = $(this);
//     let product_id = $(this).data("product")
//     console.log("hai")
//     console.log(product_id);

//     $.ajax({
//         url: '/delete-product-from-cart',
//         data: {
//             'id': product_id,
//         },
//         dataType: 'json',
//         beforeSend: function(){
//             console.log("Deleting")
//         },
//         success:function(response){
//             $(".cart-item-count").text(response.totalcartitems)
//             $("#cart-products").html(response.data)
//             location.reload();
//         }
//     });
// });
