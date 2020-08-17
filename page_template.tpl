<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" 
  "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Тег TD</title>
 </head>
 <body>

    <table border="1" cellpadding="7" cellspacing="0">
    
	<tr>
    <th colspan="2" bgcolor="#D3EDF6" align="center">Ф.И.О</th>
    <th colspan="3" bgcolor="#D3EDF6" align="center">Номер и серия паспорта</th>
    <th colspan="4" bgcolor="#D3EDF6" align="center">ИНН</th>
    <th colspan="5" bgcolor="#D3EDF6" align="center">Дата рождения</th>
	<th colspan="6" bgcolor="#D3EDF6" align="center">Дата поподания в черный список</th>
	<th colspan="7" bgcolor="#D3EDF6" align="center">Дата выхода из черного списка</th>
	<th colspan="8" bgcolor="#D3EDF6" align="center">Организация</th>
	<th colspan="9" bgcolor="#D3EDF6" align="center">Причина поподания в черный список</th>
	<th colspan="10" bgcolor="#D3EDF6" align="center">Купленный товар</th>
	<th colspan="11" bgcolor="#D3EDF6" align="center">Сумма долга</th>
    </tr>
	
    <tr>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>10</td>
    <td>11</td>
    </tr>   
   
	</table> 

 </body>
</html>



<b>Дата рождения!<b>
<p>{{person_date}}</p>

<b>Дата поподания в черный список<b>
<p>{{black_date}}</p>

<b>Дата выхода из черного списка<b>
<p>{{end_black_date}}</p>

<b>Организация!<b>
<p>{{org_name}}</p>

<b>Коментарии!<b>
<p>{{coment}}</p>

<b>Купленный товар!<b>
<p>{{tovar}}</p>


<b>Сумма долга<b>
<p>{{dolg}}</p>
% end