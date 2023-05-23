<template>
  <div class="content">
    <Header/>


    <h2 class="calendar-title">{{ displayDate }}</h2>
    <div class="button-area">
      <button @click="prevMonth" class="button">前の月</button>
      <button @click="nextMonth" class="button">次の月</button>
    </div>
    <div class="calendar">
      <div class="calendar-weekly">
    <div class="calendar-youbi" v-for="n in 7" :key="n">
      {{ youbi(n-1) }}
    </div>
    </div>
      
      <div 
        class="calendar-weekly"
        v-for="(week, index) in calendars"
        :key="index"
      >
        <div
          class="calendar-daily"
          :class="{outside: currentMonth !== day.month}" 
          v-for="(day, index) in week"
          :key="index"
        >
          <div class="calendar-day">
            {{ day.day }}
          </div>
          <div v-for="dayEvent in day.dayEvents" :key="dayEvent.id" >
    <div 
      class="calendar-event"
      :style="`background-color:${dayEvent.color}`" >
      {{ dayEvent.name }}
    </div>
  </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import moment from "moment";
export default {
name: "Calendar",
components:{
    Header
},
  data() {
    return {
      currentDate: moment(),
      events:[
  { id: 1, name: "今日の日記", start: "2023-05-04", end:"2023-05-04", color:"blue"},
  ]
    };
  },
  methods: {
    getStartDate() {
      let date = moment(this.currentDate);
      date.startOf("month");
      const youbiNum = date.day();
      return date.subtract(youbiNum, "days");
    },
    getEndDate() {
      let date = moment(this.currentDate);
      date.endOf("month");
      const youbiNum = date.day();
      return date.add(6 - youbiNum, "days");
    },
    getDayEvents(date){
      return this.events.filter(event => {
      let startDate = moment(event.start).format('YYYY-MM-DD')
      let endDate = moment(event.end).format('YYYY-MM-DD')
      let Date = date.format('YYYY-MM-DD')
      if(startDate <= Date && endDate >= Date) return true;
     });
    },
    getCalendar() {
      let startDate = this.getStartDate();
      const endDate = this.getEndDate();
      const weekNumber = Math.ceil(endDate.diff(startDate, "days") / 7);

      let calendars = [];
      let calendarDate = this.getStartDate();

      for (let week = 0; week < weekNumber; week++) {
        let weekRow = [];
        for (let day = 0;  day < 7; day++) {
          let dayEvents = this.getDayEvents(calendarDate)
          weekRow.push({
            day: calendarDate.get("date"),
            month: calendarDate.format("YYYY-MM"),
            dayEvents
          });
          calendarDate.add(1, "days");
        }
        calendars.push(weekRow);
      }
      return calendars;
    },
    nextMonth() {
      this.currentDate = moment(this.currentDate).add(1, "month");
    },
    prevMonth() {
      this.currentDate = moment(this.currentDate).subtract(1, "month");
    },
    youbi(dayIndex) {
    const week = ["日", "月", "火", "水", "木", "金", "土"];
    return week[dayIndex];
    },
  },
  computed: {
    calendars() {
      return this.getCalendar();
    },
    displayDate(){
      return this.currentDate.format('YYYY[年]M[月]')
    },
    currentMonth(){
    return this.currentDate.format('YYYY-MM')
    },
  },
  
}
</script>

<style>
.content{
  margin:2em auto;
  width:100%;
}
.button-area{
  margin:0.5em 0;
}
.button{
  padding:4px 8px;
  margin-right:8px;
}
.calendar{
  max-width:100%;
  border-top:1px solid #E0E0E0;
  font-size:0.8em;
}
.calendar-weekly{
  display:flex;
  border-left:1px solid #E0E0E0;
  /* background-color: black; */
}
.calendar-daily{
  flex:1;
  min-height:125px;
  border-right:1px solid #E0E0E0;
  border-bottom:1px solid #E0E0E0;
  margin-right:-1px;
}
.calendar-day{
  text-align: center;
}
.calendar-youbi{
  flex:1;
  border-right:1px solid #E0E0E0;
  margin-right:-1px;
  text-align:center;
}
.outside{
  background-color: #f7f7f7;
}
.calendar-event{
  color:white;
  margin-bottom:1px;
  height:50px;
  line-height:25px;
}
.calendar-title {
  font-family: sans-serif;
  font-size: 2em;
  font-weight: bold;
}
.calendar-event{
  color:white;
  margin-bottom:1px;
  height:50px;
  line-height:25px;
  position: relative;
  z-index:1;
  border-radius:4px;
  padding-left:4px;
}
</style>