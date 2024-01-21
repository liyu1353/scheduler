import Image from 'next/image'

import Calendar from './calendar.js'


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
