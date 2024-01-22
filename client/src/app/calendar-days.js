'use client'
import GSheetReader from 'g-sheets-api';

const options = {
    apiKey: 'AIzaSyD4LnmU8PudTtBQ7JOr60zsltPktF9FtrM',
    sheetId: '1MdxRxvXXiE8_k_2_wr4_U70fBVt5j4WY137z9Pnj8qQ',
    sheetNumber: 1,
    sheetName: 'Sheet1', // if sheetName is supplied, this will take precedence over sheetNumber
    returnAllResults: false
}

function Popup() {

}

function Clicked(props, day){
    props.changeCurrentDay(day);
    console.log("Clicked")
    GSheetReader(options, (results) => {
        console.log(results.length);
        for(let i = 0; i < results.length; i++){
            //console.log(results[i]["Date"]);
            const dateCopy = new Date(day.date.getTime());
            dateCopy.setTime(day.date.getTime() - 5 * 60 * 60 * 1000);
            const date = new Date(results[i]["Date"]);
            console.log(date);
            console.log(dateCopy);
            if(date.toDateString() === dateCopy.toDateString()){
                console.log("matches today");
            }
        }
        console.log(day)
    }).catch((err) => {

    });
}

function CalendarDays(props) {
    let firstDayOfMonth = new Date(props.day.getFullYear(), props.day.getMonth(), 1);
    let weekdayOfFirstDay = firstDayOfMonth.getDay();
    let currentDays = [];

    for (let day = 0; day < 42; day++) {
        if (day === 0 && weekdayOfFirstDay === 0) {
            firstDayOfMonth.setDate(firstDayOfMonth.getDate() - 7);
        } else if (day === 0) {
            firstDayOfMonth.setDate(firstDayOfMonth.getDate() + (day - weekdayOfFirstDay));
        } else {
            firstDayOfMonth.setDate(firstDayOfMonth.getDate() + 1);
        }

        let calendarDay = {
            currentMonth: (firstDayOfMonth.getMonth() === props.day.getMonth()),
            date: (new Date(firstDayOfMonth)),
            month: firstDayOfMonth.getMonth(),
            number: firstDayOfMonth.getDate(),
            selected: (firstDayOfMonth.toDateString() === props.day.toDateString()),
            year: firstDayOfMonth.getFullYear()
        }

        currentDays.push(calendarDay);
    }

    return (
        <div className="table-content">
            {
                currentDays.map((day) => {
                    return (
                        <div className={"calendar-day" + (day.currentMonth ? " current" : "") + (day.selected ? " selected" : "")}
                             onClick={() => Clicked(props, day)}>
                            <p>{day.number}</p>
                        </div>
                    )
                })
            }
        </div>
    )
}



export default CalendarDays;