/* Followed videos in course */
var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create("card" );
card.mount("#card-element");

/* Handles realtime validation errors on card element */

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fa fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

/* Sumit Form - From Stripe Docs and course videos */

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
	    /* ev.preventDefault();
	    card.update({ 'disabled': true});*/
        $('#submit-btn').attr('disabled', true);
        
	    var saveInfo = Boolean($('#id-save-info').attr('checked'));
	    // From using {% csrf_token %} in the form
	    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
	    var postData = {
	        'csrfmiddlewaretoken': csrfToken,
	        'client_secret': clientSecret,
	        'save_info': saveInfo,
	    };
	    var url = '/checkout/cache_checkout/';
	
	    $.post(url, postData).done(function() {
	        stripe.confirmCardPayment(clientSecret, {
	            payment_method: {
	                card: card,
	                billing_details: {
	                    name: $.trim(form.full_name.value), 
	                    phone: $.trim(form.telephone.value),
	                    email: $.trim(form.email.value),
	                    address:{
	                        line1: $.trim(form.address1.value),
                            line2: $.trim(form.address2.value),
                            city: $.trim(form.county.value),
	                    }
	                }
	            },
	            shipping: {
	                name: $.trim(form.full_name.value),
	                address: {
	                    line1: $.trim(form.address1.value),
                        line2: $.trim(form.address2.value),
	                    city: $.trim(form.county.value),
	                    postal_code: $.trim(form.postcode.value),
	                }
	            },
	        }).then(function(result) {
	            if (result.error) {
	                var errorDiv = document.getElementById('card-errors');
	                var html = `
	                    <span class="icon" role="alert">
	                    <i class="fa fa-times"></i>
	                    </span>
	                    <span>${result.error.message}</span>`;
	                $(errorDiv).html(html)
	                $('#submit-btn').attr('disabled', false);
	            } else {
	                if (result.paymentIntent.status === 'succeeded') {
	                    form.submit();
	                }
	            }
	        });
	    })
	});