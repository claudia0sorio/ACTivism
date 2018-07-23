YUI().use('calendar', function (Y) {

});






YUI().use('calendar', function (Y) {

  var calendar = new Y.Calendar({
          contentBox: "#mycalendar",
          height:'400%',
          width:'100%',
          showPrevMonth: true,
          showNextMonth: true,
          date: new Date(2018,7,0)}).render();

});
