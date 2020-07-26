      // scripts for add recipe form
      var itemRowCount = 1;
      var itemCount = 0;
      var stepCount = 1;

      function copy1frominput(table, input) {
        var AddRow = document.getElementById(table);
        var NewRow = AddRow.insertRow(-1);
        input_in_table = document.getElementById(input).value;
        var cel1 = NewRow.insertCell(0);
        cel1.innerHTML = input_in_table;
        document.getElementById(input).value = "";
      }

      function copy2frominput(table, input, input2) {
        var AddRow = document.getElementById(table);
        var NewRow = AddRow.insertRow(-1);
        input_in_table = document.getElementById(input).value;
        input_in_table2 = document.getElementById(input2).value;
        var cel1 = NewRow.insertCell(0);
        var cel2 = NewRow.insertCell(1);
        cel1.innerHTML = input_in_table;
        cel2.innerHTML = input_in_table2;
        document.getElementById(input).value = "";
        document.getElementById(input2).value = "";
      }

      function copycookiename() {
        copy1frominput("cookie_name_table", "cookie_name");
      }

      function addtoingredienttable() {
        copy2frominput("ingredient_table", "qty", "ingredient");
      }

      function copyauthor() {
        copy2frominput("author_table", "firstname", "lastname");
      }

      function addtostepstable() {
        var AddRow = document.getElementById("steps_table");
        var NewRow = AddRow.insertRow(-1);
        steps_in_table = document.getElementById("steps").value;
        var cel1 = NewRow.insertCell(0);
        var cel2 = NewRow.insertCell(1);
        cel1.innerHTML = stepCount + ". ";
        cel2.innerHTML = steps_in_table;
        stepCount = stepCount + 1;
        document.getElementById("steps").value = "";
      }

      // script for materialize box enlargement on editrecipe.html and addrecipe.html
      document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('.materialboxed');
            var instances = M.Materialbox.init(elems, options);
        });
