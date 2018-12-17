$(document).ready(function() {
    var form = $('.formBuyProduct');
    // var clikForm = $(this);
    // console.log(clikForm);
    function basketUpdating(product_id, numb, is_delete){

        var data  = {};
        data.product_id = product_id;
        data.numb = numb;
        var csrf_token = $('.formBuyProduct [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");
        if (is_delete){
           data["is_delete"] = true;
        }
        console.log(url);
        console.log("=>");
        console.log(data);

        $.ajax({
           url: url,
           type: "POST",
           data: data,
           cache: true,
           success: function (data) {
               console.log("data");
               console.log("OK");
               console.log(data.products_total_nmb);
               if (data.products_total_nmb || data.products_total_nmb == 0){
                    $('.basketTotalNmb').text("("+data.products_total_nmb+")");
                    console.log(data.products);
                    $('.tableBasket tbody').html("");
                    $.each(data.products, function(k, v){
                        $('.tableBasket').append('<tr><td>'+v.product_name+'</ td><td>'+v.numb+' шт.</td><td> по '+v.price_per_item+' руб.</ td><td><a class="delete-item" href="#" data-product_id="'+v.id+'">X</a></td></ tr>');
                    });
                };
           },
           error: function(){
               console.log("error");
           },

        });

    }

    form.on('submit', function(e){
        e.preventDefault();
        console.log($(this));
        console.log("inb");
        var clikedForm = $(this).find('.inBuyProduct');
        console.log(clikedForm);
        console.log("inb");

        var numb = clikedForm.val();
        console.log("numb");
        console.log(numb);
        console.log("numb");

        var in_buy_btn = $(this).find('.inBuyBtn');

        console.log("in");
        console.log(in_buy_btn);
        var product_name = in_buy_btn.data("product_name");
        var product_id = in_buy_btn.data("product_id");
        var product_price = in_buy_btn.data("product_price");
        console.log(product_name);
        console.log(product_id);
        console.log(product_price);
        basketUpdating(product_id, numb, is_delete=false)
    });

    function reshowBasket(){

        $('.dropdown-menu').addClass('show');
    };
    //
    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        product_id = $(this).data("product_id")
        numb = 0;
        basketUpdating(product_id, numb, is_delete=true)
        reshowBasket();
    });
});
