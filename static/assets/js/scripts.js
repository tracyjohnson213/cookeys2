// scripts for add recipe form
      
      function copycookiename() {
        document.getElementById("cookie_name").innerHTML = document.getElementById("cookie_name").value
      }

      function addtoingredienttable() {
        // takes qty and ingredient input to fill ingredient_table
        document.getElementById("qty").innerHTML = document.getElementById("qty_in_table").value
        document.getElementById("ingredient").innerHTML = document.getElementById("ingredient_in_table").value
      }

      function addtostepstable() {
        // takes steps input to fill steps_table
        document.getElementById("steps").innerHTML = document.getElementById("steps_in_table").value
        addRowCount('.steps_table');
      }

      function addRowCount(tableAttr) {
        // https://mariusmateoc.com/blog/automatic-serial-number-row-in-html-table/
        // auto number row in table
        $(tableAttr).each(function(){
            $('td#steps_table', this).each(function(i){
            $(this).before('<td>'+(i+1)+'</td>');
            });
        });
      }

      function copyfirstname() {
        // takes inputted first and last names and copies to table
        document.getElementById("firstname").innerHTML = document.getElementById("firstname_in_table").value
      }

      function copylastname() {
        // takes inputted first and last names and copies to table
        document.getElementById("lastname").innerHTML = document.getElementById("lastname_in_table").value
      }

      function copyauthor(){
        copyfirstname();
        copylastname();
      }
