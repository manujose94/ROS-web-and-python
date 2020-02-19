//Table
var row_okey;
var tagsArray;
var selected_row;
var array_robots = [];
var topic_selected={name:"",type:"",date_init:""};

window.onload = function () {
    this.console.log("[view.js] View loaded ")

   
}


function filloutTable(array/** topic names */, array2/** topic type */) {
    if (!array || !array2) return;
    if ($("#mytable tbody").length == 0)
        $("#mytable").append("<tbody></tbody>");
    $("#mytable tbody tr").remove();
    // Append product to the table
    for (var i = 0; i < array.length; i++) {
        var fields = array[i].split('/');
        if (fields[1]) array_robots.push(fields[1]);
        //console.log(fields)
        $("#mytable tbody").append(
            '<tr class="w3-hover-text-green">' +
            "<td>" + fields[1] + "</td>" +
            "<td>" + array[i] + "</td>" +
            "<td>" + array2[i] + "</td>" +
            "</tr>"
        );

        let rows = document.getElementsByTagName("tr");
        for (var i = 0; i < rows.length; i++) {
            rows[i].onclick = function () {
                if (!this) return;
                if (selected_row) selected_row.style.backgroundColor = "white";
                selected_row = this;
                console.log(this);
                this.style.backgroundColor = "#D5E9FF";
                document.getElementById('modal_header').innerText = selected_row.cells[0].innerText;
                document.getElementById('modal_text').innerText = selected_row.cells[1].innerText;
                document.getElementById('modal_text2').innerText = selected_row.cells[2].innerText;
                document.getElementById('modal_connect_button').innerText = 'Connecto to:'+selected_row.cells[1].innerText;
                document.getElementById('id01').style.display = 'block'
                topic_selected.name=selected_row.cells[1].innerText;
                topic_selected.type=selected_row.cells[2].innerText;
                topic_selected.date_init=getCurrentDate()

                console.log("topic_selected",topic_selected)
            }
        }

        var uniq = array_robots.slice() // slice makes copy of array before sorting it
            .sort(function (a, b) {
                return a > b;
            })
            .reduce(function (a, b) {
                if (a.slice(-1)[0] !== b) a.push(b); // slice(-1)[0] means last item in array without removing it (like .pop())
                return a;
            }, []); // this empty array becomes the starting value for a
        
        document.getElementById("count_r").innerHTML = uniq.length;
        document.getElementById("count_t").innerHTML = array.length;
    }

}



function getCurrentDate(){
    let  d = new Date();
    let date_format= ("0" + d.getDate()).slice(-2) + "-" + ("0"+(d.getMonth()+1)).slice(-2) + "-" +
    d.getFullYear() + " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2) +":" + ("0" + d.getSeconds()).slice(-2);
    return date_format;
}

function addViewNewSubs(objRos){
    let {name, messageType} =objRos;
    let simplename=getNodeName_fromNameTopic(name);
    console.log({simplename})
    let id1="x";let id2="y"
        let sus_names='<div id="'+simplename+'"><p> X '+simplename+' pose:</p>'+
                      '<p>Y '+simplename+' pose:</p></div>'
        //var para = document.createElement(sus_names);

        document.getElementById("subs_names").innerHTML += sus_names;
     
 }

 function getNodeName_fromNameTopic(name){
    if(name)return name.split("/")[1]
    else return null;
 }