
<XML ID="users">
    <?xml version="1.0"?>
    <users>
        <users>
            <TITLE> users </TITLE>
            <PRICE> 10.00 </PRICE>
        </users>
        <users>
            <TITLE> Prod#2 </TITLE>
            <PRICE> 20.00 </PRICE>
        </users>
    </users>
</XML> 


<b>Зарегистрированное имя в системе <b>
% for item in personname[0]:
 <div>{{personname}}</div>

<b>Номер и серия паспорта<b>
<p>{{passport_id}}</p>

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