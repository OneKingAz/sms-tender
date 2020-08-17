<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML  4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Тег TABLE</title>
 </head>
 <body>
  <table border="10" width="100%" cellpadding="5">
   <tr>
    <th>Ф.И.О</th>
    <th>Серия и номер паспорта</th>
    <th>ИНН</th>
    <th>Дата рождения</th>
    <th>Дата поподания в черный список</th>
    <th>Дата выхода из черного списка</th>
    <th>Организация</th>
    <th>Причина поподания в черный список</th>
    <th>Купленный товар</th>
    <th>Сумма</th>
    <th>Порядковый номер</th>


   </tr>
   <tr>
    <td>
     <ul>
    <p>{{personname}}</p>
</ul>
    </td>


    <td>
     <ul>

    <p>{{passport_id}}</p>

</ul>
    </td>


    <td>
     <ul>

    <p>{{value}}</p>

</ul>
    </td>


    <td>
 <ul>

    <p>{{person_date}}</p>

</ul>
    </td>


    <td>
 <ul>

    <p>{{black_date}}</p>

</ul>
    </td>


    <td>
     <ul>

    <p>{{end_black_date}}</p>

</ul>
    </td>
    <td>
     <ul>

    <p>{{org_name}}</p>

</ul>
    </td>


    <td>
     <ul>
 
    <p>{{coment}}</p>

</ul>
    </td>


    <td>
     <ul>
 
    <p>{{tovar}}</p>

</ul>
    </td>


    <td>
     <ul>

    <p>{{dolg + " сом"}}</p>

</ul>
</td>

 <td>
     <ul>
 
    <p>{{id}}</p>

</ul>
    </td>

  </tr> 
 </table>
 </body>
</html>