
<template>

    <head>
      <title>Randomiary</title>
    </head>

    <body>
      <div class="menu">
        <h1>dAIary</h1>
        <div>
          <span class="menu-item">プロファイル</span>
          <span class="menu-item">日記作成</span>
        </div>
      </div>

      <div class="calendar">
        <div id="app">
          <full-calendar :events="events" :config="calendarConfig"></full-calendar>
        </div>
      </div>

    </body>

</template>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js">
</script>
<script src="https://cdn.jsdelivr.net/npm/vue-full-calendar@2.8.0/dist/vue-full-calendar.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/vue-full-calendar@2.8.0/dist/fullcalendar.min.css">

<script>
export default {
    name: "calendar"
}

  new Vue({
        el: '#app',
        data() {
            return {
                events: [
                    {
                        title: 'Event 1',
                        start: '2023-05-01'
                    },
                    {
                        title: 'Event 2',
                        start: '2023-05-05',
                        end: '2023-05-07'
                    }
                ],
                calendarConfig: {
                    // 配置项
                }
            };
        },
        components: {
            'full-calendar': VueFullCalendar.default
        }
    });

</script>

<style scoped>

.menu {
			display: flex;
			justify-content: space-between;
			align-items: center;
			background-color: #f1f1f1;
			height: 50px;
			padding: 0 20px;
		}

		.menu-item {
			font-size: 18px;
			padding: 10px 20px;
			cursor: pointer;
		}

</style>