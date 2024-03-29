/* jshint esversion: 11 */

// Materialize sidenav initialization
document.addEventListener('DOMContentLoaded', function() {
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);
});

// Materialize modal initialization
document.addEventListener('DOMContentLoaded', function() {
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);
});

// Materialize dropdown list initialization
document.addEventListener('DOMContentLoaded', function() {
  let dropdown = document.querySelectorAll('select');
  M.FormSelect.init(dropdown);
});

// Materialize datepicker initialization
document.addEventListener('DOMContentLoaded', function() {
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmm yyyy",
    yearRange: 100,
    i18n: {done: "Select"}
  });
});