$(function(){

    $('body').on('change','.related-widget-wrapper select',function(){

        var id = $(this).val();
        var button = $(this).siblings('.related-widget-wrapper-link.change-related');

        if(button.length){

            var base = $(button).attr('href-base');

            if( base.indexOf('__id__')==-1 ){
                button.attr('href', base + id );
            } else {
                button.attr('href', base.replace('__id__',id ) );
            }

            if( id ){
                button.show();
            } else {
                button.hide();
            }

        }

    });


    $('.related-widget-wrapper select').change();

});

