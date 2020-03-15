$(document).ready(function() {
    $('#date-picker').datetimepicker({
        timepicker: false,
        datepicker: true,
        format: 'm/d/yy'
    });
    $('#date-picker').datetimepicker('setDate', 'today');
})