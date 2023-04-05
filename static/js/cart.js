      // Check whether the item is in the cart or not
      if (localStorage.getItem("cart") == null) {
        cart = {};
        // if it is in
      } else {
        cart = JSON.parse(localStorage.getItem("cart"));
        document.getElementById("cart-num").innerHTML =
          Object.keys(cart).length;
      }

      // when the cart button is clicked get the clicked btn id
      $(".cart").click(function () {
        // console.log("working");
        var idstr = this.id.toString();
        console.log(idstr);

        if (cart[idstr] != undefined) {
          cart[idstr] = cart[idstr] + 1;
        } else {
          cart[idstr] = 1;
        }
        console.log(cart);
        // Add the items in the local storage in the form of string
        localStorage.setItem("cart", JSON.stringify(cart));
      });

      updatePopover(cart);
      function updatePopover(cart) {
        // console.log('popover')
        var popstr = "";
        var i = 1;
        popstr = popstr +
        "<div class='row'>" +
         "<h5 class='pop_head col-6'>Cart</h5>" +
         "<button>Clear Cart</button>" +
         "</div>"+
         "<div class='cart_product m-3'>"
         ;
        for (var item in cart) {
          popstr = popstr + "<div class='mini_cart_item'>"
          popstr = popstr + "<b>" + i + "." + "</b> ";
          popstr = popstr +  
            document.getElementById("img" + item).innerHTML +
            "<h5 class='pr_name'>" +
            document.getElementById("name" + item).innerHTML + 
            "<br>" +
            " Qty: " +
            cart[item] +
            "</h5>" +
            "</div>"+
            "<br>";
          i = i + 1;
        }
        popstr = popstr + "</a></div>";


        var popoverTriggerList = [].slice.call(
          document.querySelectorAll('[data-bs-toggle="popover"]')
        );
        var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
          return new bootstrap.Popover(popoverTriggerEl);
        });

        document
          .getElementById("popcart")
          .setAttribute("data-bs-content", popstr);
      }