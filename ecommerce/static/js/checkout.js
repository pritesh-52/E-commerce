 $(document).ready(function(){

    $('.payWithRazorpay').click(function(e){
        e.preventDefault();
        var fname=$("[name='fname']").val();
        var lname=$("[name='lname']").val();
        var email=$("[name='email']").val();
        var phone=$("[name='phone']").val();
        var address=$("[name='address']").val();
        var city=$("[name='city']").val();
        var state=$("[name='state']").val();
        var country=$("[name='country']").val();
        var pincode=$("[name='pincode']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();


        if (fname==""||lname==""||email==""||phone==""||address==""||city==""||state==""||country==""||pincode=="")
        {
            swal("Alert", "All fileds are required", "error");
            return false;
        }

        else{

            $.ajax({
                type:"GET",
                url:"/proceed-to-pay",
                success:function(response){
                    //console.log(res)
                    var options = {
                        "key": "rzp_test_RaGye25HXAWc2Y", // Enter the Key ID generated from the Dashboard
                        /*"amount": response.total_price*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise*/
                        "amount":1*100,
                        "currency": "INR",
                        "name": "Fashion wear",
                        "description": "Thank you for buy shopping with us ",
                        "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG9ubGluZSUyMHNob3B8ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60",
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);  
                            data={
                                 "fname":fname,
                                 "lname":lname,
                                 "email":email,
                                 "phone":phone,
                                 "address":address,
                                 "city":city,
                                 "state":state,
                                 "country":country,
                                 "pincode":pincode,
                                 "payment_mode":"Paid by Razorpay",
                                 "payment_id":responseb.razorpay_payment_id,
                                 csrfmiddlewaretoken: token,
                            } 
                            $.ajax({
                                method:"POST",
                                url:"/place-order",
                                data:data,
                                
                                success:function(responsec){
                                    swal("Congrulationes", responsec.status, "success").then((value) => {
                                        window.location.href="/my-orders"
                                      });

                                }
                            })  
                        },
                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact": phone,
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();

                }
            });
            

        }


        

    });
 })