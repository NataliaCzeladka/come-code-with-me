$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $('.materialboxed').materialbox();
  $('.tooltipped').tooltip();
  $(".datepicker").datepicker({
    format: "dd mmmm, yyyy",
    yearRange: 0,
    i18n: {
      done: "Select"
    }
  });
});