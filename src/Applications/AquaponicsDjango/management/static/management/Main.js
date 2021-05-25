function changeColor(){
    let table = document.getElementById("table");
    let rowLength = table.rows.length;
    let row = table.rows;

    var tableData = document.getElementById("table").getElementsByTagName("td");

    for (i = 1; i < rowLength; i++){
        //gets cells of current row
        let oCells = table.rows.item(i).cells;
        let cellVal = oCells.item(1).innerHTML;

        switch(i){
            case 1:
                if(cellVal < 1.0){
                    tableData[1].style.backgroundColor = "#0AFC48aa";
                }
                else if(cellVal > 1.0 && cellVal < 1.5){
                    tableData[2].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal >= 1.50){
                    tableData[3].style.backgroundColor = "#FE2A0Faa";
                }
                break;
            case 2:
                if(cellVal > 27 && cellVal<= 29){
                    tableData[5].style.backgroundColor = "#0AFC48aa";
                }
                else if(cellVal > 18 && cellVal<=27){
                    tableData[6].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal > 29){
                    tableData[7].style.backgroundColor = "#FE2A0Faa";
                }
                break;
            case 3:
                if(cellVal > 6.8 && cellVal<=7.0){
                    tableData[9].style.backgroundColor = "#0AFC48aa";
                }
                else if((cellVal > 6.4 && cellVal<=6.8) || (cellVal > 7.0 && cellVal<=7.4) ){
                    tableData[10].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal > 7.4 || cellVal < 6.4){
                    tableData[11].style.backgroundColor = "#FE2A0Faa";
                }
                break;
            case 4: 
                if(cellVal > 6.5){
                    tableData[13].style.backgroundColor = "#0AFC48aa";
                }
                else if(cellVal > 4.5 && cellVal<=6.5){
                    tableData[14].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal < 4.5){
                    tableData[15].style.backgroundColor = "#FE2A0Faa";
                }
                break;
            case 5:
                if(cellVal > 0.5 && cellVal <= 1.0){
                    tableData[17].style.backgroundColor = "#0AFC48aa";
                }
                else if(cellVal > 0.1 && cellVal<=0.5){
                    tableData[18].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal > 1.0 || cellVal < 0.1){
                    tableData[19].style.backgroundColor = "#FE2A0Faa";
                }
                break;
            case 6:
                if(cellVal > 10.0 && cellVal<=100){
                    tableData[21].style.backgroundColor = "#0AFC48aa";
                }
                else if((cellVal > 5 && cellVal<=10) || (cellVal > 100 && cellVal < 450)){
                    tableData[22].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal > 450 || cellVal < 5){
                    tableData[23].style.backgroundColor = "#FE2A0Faa";
                }
                break;
            case 7:
                if(cellVal > 70 && cellVal<=80){
                    tableData[25].style.backgroundColor = "#0AFC48aa";
                }
                else if((cellVal > 50 && cellVal<=70) || (cellVal > 80 && cellVal<=85)){
                    tableData[26].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal > 85 || cellVal < 50){
                    tableData[27].style.backgroundColor = "#FE2A0Faa";
                }
                break;
            case 8:
                if(cellVal > 0.0 && cellVal<=0.3){
                    tableData[29].style.backgroundColor = "#0AFC48aa";
                }
                else if(cellVal > 0.3 && cellVal<=0.5){
                    tableData[30].style.backgroundColor = "#FFF719aa";
                }
                else if(cellVal > 0.5){
                    tableData[31].style.backgroundColor = "#FE2A0Faa";
                }
                break;

        }
    }
}

changeColor();