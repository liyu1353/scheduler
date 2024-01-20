import Image from 'next/image'

import GSheetReader from 'g-sheets-api';
import Calendar from './calendar.js'

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

export default function Home() {
    return (
        <>
            <style>
                {`
          body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: lightblue;
          }

          nav {
            background-color: lightblue;
            padding: 10px;
            text-align: center;
          }

          section {
            background-color: white;
            padding: 400px;
            text-align: center;
            color: black;
          }

          calendar-module {
            /* Your styling for the calendar module goes here */
          }
        `}
            </style>

            <nav>
                {/* Your navigation links go here */}
                <a href="#">Calendar</a> |
                <a href="#">About</a> |
                <a href="#">Contact</a>
            </nav>

            <section>
                <h2>Calendar</h2>

                <div id="calendar-module">
                    <Calendar>
                    </Calendar>
                </div>
            </section>
        </>
    );
}
