function childIndex(elem){
    children = elem.parentNode.childNodes;

    i=0;
    for(child in children){
        if(children[child].nodeName=='TR') i++;
        if(children[child]==elem) return i;
    }
}

function print_r(obj){
    for(el in obj){
        console.log(el+': '+obj[el]);
    }
}

$(function (){
    $("#addRow").click(function(){
        rows++;
        addRow();
        return false;
    });

    $("#addCowText").click(function(){
        cows++;
        addCow();
        console.log(cows);
        return false;
    });

    $(".delRow").live("click", function(){
        rows--;
        delRow(this.parentNode.parentNode.parentNode);
        return false;
    });


    $(".delCow").live("click", function(){
        cows--;
        delCow(this.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode);
        return false;
    });  

    function delRow(row){
        index = childIndex(row);
        section = row.parentNode;
        section.removeChild(row);
        rows_arr = section.getElementsByTagName('tr');
        for(i=index;i<=rows_arr.length; i++){
            rows_arr[i-1].id = "row"+i;
            cells = rows_arr[i-1].getElementsByTagName('td');
            cells[0].innerHTML=i;
            cells[1].childNodes[0].name='Form_table['+i+'][date]'; 
            cells[2].childNodes[0].name='Form_table['+i+'][desc]'; 
            cells[3].childNodes[0].name='Form_table['+i+'][place]'; 
        }
    }

    function delCow(ww){
        index = childIndex(ww);
        index;
        section = ww.parentNode;
        section.removeChild(ww);
        wws_arr = $('#coworkers div.ww')
        console.log(wws_arr);
        for(i=index;i<=wws_arr.length; i++){
            if (wws_arr[i].id=='addCow') break;
            if (wws_arr[i].id=='addCow') break;
            cells = wws_arr[i].getElementsByTagName('td');
            cells[0].childNodes[0].name='Form_cow['+(i+1)+'][fio]'; 
            cells[2].childNodes[0].name='cow['+(i+1)+'][birthdate]'; 
            cells[3].childNodes[0].name='cow['+(i+1)+'][study]'; 
            cells[4].childNodes[0].name='cow['+(i+1)+'][contacts]'; 
        }
    }

    function addRow(){
        var newtr=document.createElement("tr");
        newtr.id="row"+rows;
        
        td_date  = document.createElement("td");
        td_desc  = document.createElement("td");
        td_place = document.createElement("td");
        td_count = document.createElement("td");
        td_del   = document.createElement("td");

        ta_date  = document.createElement("textarea");
        ta_desc  = document.createElement("textarea");
        ta_place = document.createElement("textarea");

        delImage = document.createElement("img");
        delImage.src = "images/minus.png";


        delA = document.createElement("a");
        delA.href = "#";
        delA.className = "delRow";
        delA.appendChild(delImage);

        del_div = document.createElement("div");
        del_div.appendChild(delA);


        ta_date.className='date';
        ta_date.name='Form_table['+rows+'][date]';

        ta_desc.className='desc';
        ta_desc.name='Form_table['+rows+'][desc]';

        ta_place.className='place';
        ta_place.name='Form_table['+rows+'][place]';

        td_del.className = "delRowTd";

        td_count.innerHTML=rows;
        td_count.className="center";

        td_date.appendChild(ta_date);
        td_desc.appendChild(ta_desc);
        td_place.appendChild(ta_place);
        td_del.appendChild(del_div);


        newtr.appendChild(td_count);
        newtr.appendChild(td_date);
        newtr.appendChild(td_desc);
        newtr.appendChild(td_place);
        newtr.appendChild(td_del);

        document.getElementById("events").appendChild(newtr);
    }


    function addCow(){
        var fio = document.createElement("input");
        fio.type = 'text';
        fio.placeholder = 'Ф.И.О.';
        fio.maxLength = 255;
        fio.name = 'Form_cow['+cows+'][fio]';
        fio_td = document.createElement("td");
        fio_td.appendChild(fio);

        delImage = document.createElement("img");
        delImage.src = "images/minus.png";
        delA = document.createElement("a");
        delA.href = "#";
        delA.className = "delCow";
        delA.appendChild(delImage);
        del_div = document.createElement("div");
        del_div.className = 'ww-minus';
        del_div.appendChild(delA);
        del_td = document.createElement("td");
        del_td.rowSpan = 4;
        del_td.appendChild(del_div);

        ftr = document.createElement("tr");
        ftr.appendChild(fio_td);
        ftr.appendChild(del_td);


        var bd = document.createElement("input");
        bd.type = 'text';
        bd.placeholder = 'Дата рождения';
        bd.maxLength = 255;
        bd.name = 'Form_cow['+cows+'][birthdate]';
        bd_td = document.createElement("td");
        bd_td.appendChild(bd);
        str = document.createElement("tr");
        str.appendChild(bd_td);

        var study = document.createElement("textarea");
        study.placeholder = 'Место учёбы (факультет, специальность, курс, группа, форма обучения: бюджетная или внебюджетная)';
        study.cols=50;
        study.rows=6;
        study.name = 'Form_cow['+cows+'][study]';
        study_td = document.createElement("td");
        study_td.appendChild(study);
        ttr = document.createElement("tr");
        ttr.appendChild(study_td);

        var cont = document.createElement("textarea");
        cont.placeholder = 'Почтовый адрес, телефон, электронный адрес';
        cont.cols=50;
        cont.rows=6;
        cont.name = 'Form_cow['+cows+'][contacts]';
        cont_td = document.createElement("td");
        cont_td.appendChild(cont);
        fotr = document.createElement("tr");
        fotr.appendChild(cont_td);

        var tb = document.createElement("tbody");
        tb.appendChild(ftr);
        tb.appendChild(str);
        tb.appendChild(ttr);
        tb.appendChild(fotr);

        var tbl = document.createElement("table");
        tbl.appendChild(tb);

        var newdiv = '';
        newdiv = document.createElement("div");
        newdiv.className='ww';
        newdiv.appendChild(tbl);

        addDiv = document.getElementById("addCow");
        $(newdiv).insertBefore("#addCow");
    }
});