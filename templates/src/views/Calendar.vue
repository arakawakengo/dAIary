<template>
  <div class="content">
    <Header/>


    <h2 class="calendar-title">{{ displayDate }}</h2>
    <div class="button-area">
      <div class="navigation-buttons">
        <button @click="prevMonth" class="button">前の月</button>
        <button @click="thisMonth" class="button">今月</button>
        <button @click="nextMonth" class="button">次の月</button>
      </div>
      <div class="date-input">
        <div class="input-wrapper">
          <select v-model="inputYear">
            <option disabled value="">Year</option>
            <option v-for="year in years" :key="year" :value="year">{{ year }}年</option>
          </select>
        </div>
        <div class="input-wrapper">
          <select v-model="inputMonth">
            <option disabled value="">Month</option>
            <option v-for="month in months" :key="month" :value="month">{{ month }}月</option>
          </select>
        </div>
        <button @click="goToMonth" class="button">Go</button>
      </div>
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
          <div class="calendar-day" :class="{ 'today': isToday(day) }">
            {{ day.day }}
          </div>
          <div v-for="dayEvent in day.dayEvents" :key="dayEvent.id" >
            <router-link :to="`/comment/${dayEvent.id}`">
            <div 
              class="calendar-event"
              :style="`background-color:${dayEvent.color}`" >
                {{ dayEvent.name }}
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import moment from "moment";
import axios from 'axios';
export default {
name: "Calendar",
components:{
    Header
},
  data() {
    return {
      currentDate: moment(),
      events:[],
      diary_list: [],
      inputYear: moment().year(),
      inputMonth: moment().month()+1 % 12,
    };
  },
  async created() {
    try {
      const token = localStorage.getItem("access");
      const response = await axios.get("http://localhost:8000/api/diaries/", {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      this.diary_list.push(response.data.diary_list);
      await this.diary_list[0].forEach(diary => {
        diary.content = diary.content.replace(/\\n/g, "\n");
        this.events.push({
          id: diary.diary_id,
          name: diary.title,
          start: this.formatDate(diary.created_at),
          end: this.formatDate(diary.created_at),
          color: "#666699"
        });
      });

      console.log(this.diary_list[0]);
    } catch (error) {
      console.error("Failed to fetch diaries.");
      console.error(error);
    }
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
    thisMonth() {
      this.currentDate = moment();
    },
    youbi(dayIndex) {
    const week = ["日", "月", "火", "水", "木", "金", "土"];
    return week[dayIndex];
    },
    formatDate(datetime) {
      const date = new Date(datetime);
      const year = date.getFullYear();
      const month = ("0" + (date.getMonth() + 1)).slice(-2);
      const day = ("0" + date.getDate()).slice(-2);
      return `${year}-${month}-${day}`;
    },
    isToday(day) {
      return moment().format("YYYY-MM-DD") === day.month + "-" + ("0" + day.day).slice(-2);
    },
    goToMonth() {
      if (this.inputYear && this.inputMonth) {
        this.currentDate = moment(`${this.inputYear}-${this.inputMonth}`, 'YYYY-MM-01');
      }
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
    years() {
      const currentYear = new Date().getFullYear();
      return Array.from({length: currentYear - 2020 + 1}, (_, i) => 2020 + i);
    },
    months() {
      return Array.from({length: 12}, (_, i) => i + 1);
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
  display: flex;
  flex-direction: column;
  align-items: center;
  margin:0.5em 0;
}
.button{
  padding:2px 4px;
  margin-right:8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.navigation-buttons{
  display: flex;
  justify-content: center;
}
.date-input{
  display: flex;
  justify-content: center;
  margin-top: 10px;
}
.input-wrapper {
  border: 1px solid #ccc;
  padding: 2px;
  margin-right: 10px;
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
  width: 100/7%;
  max-width: 100/7%;
  overflow: hidden;
}
.today {
  background-color: #D6FF58; 
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
.calendar-title {
  font-family: sans-serif;
  font-size: 2em;
  font-weight: bold;
}
.calendar-event{
  color:white;
  margin-bottom:1px;
  height:40px;
  line-height:20px;
  position: relative;
  z-index:1;
  border-radius:4px;
  padding-left:4px;
}
</style>