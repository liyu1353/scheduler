'use client'

import GSheetReader from 'g-sheets-api';
import React, { Component } from 'react';
import CalendarDays from "./calendar-days";
import './calendar.css'

const options = {
    apiKey: 'AIzaSyD4LnmU8PudTtBQ7JOr60zsltPktF9FtrM',
    sheetId: '1MdxRxvXXiE8_k_2_wr4_U70fBVt5j4WY137z9Pnj8qQ',
    sheetNumber: 1,
    sheetName: 'Scheduler Database', // if sheetName is supplied, this will take precedence over sheetNumber
    returnAllResults: false
}

function Retriever() {
    GSheetReader(
        options,
        results => {

            // do something with the results here
        },
        error => {
            // OPTIONAL: handle errors here
        });
}

export default class Calendar extends Component {
    constructor() {
        super();

        this.weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        this.months = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'];

        this.state = {
            currentDay: new Date()
        }
    }

    render() {
        return (
            <div className="calendar">
                <div className="calendar-header">
                    <h2>{this.months[this.state.currentDay.getMonth()]} {this.state.currentDay.getFullYear()}
                    </h2>
                </div>
                <div className="calendar-body">
                    <div className="table-header">
                        {
                            this.weekdays.map((weekday) => {
                                return <div className="weekday"><p>{weekday}</p></div>
                            })
                        }
                    </div>
                    <CalendarDays day={this.state.currentDay} changeCurrentDay={this.changeCurrentDay} />
                </div>
            </div>
        )
    }
}