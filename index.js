const GSheetReader = require('g-sheets-api');

const options = {
    apiKey: 'AIzaSyD4LnmU8PudTtBQ7JOr60zsltPktF9FtrM',
    sheetId: '1MdxRxvXXiE8_k_2_wr4_U70fBVt5j4WY137z9Pnj8qQ',
    sheetNumber: 1,
    sheetName: 'Scheduler Database', // if sheetName is supplied, this will take precedence over sheetNumber
    returnAllResults: false
}
function Top() {
    return (
        <button>Test...</button>
    );
}

function Calendar(){
    //calendar code i guess
    // sheet key: 1MdxRxvXXiE8_k_2_wr4_U70fBVt5j4WY137z9Pnj8qQ
    GSheetReader(options, results =>{

    });
}

export default function Scheduler(){
    return(
        <div>
            <h1>Hello!</h1>
            <Top />
        </div>
    );
}