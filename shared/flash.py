from flask import flash

def success(message):
    return flash(message, 'success')

def danger(message):
    return flash(message, 'danger')

def info(message):
    return flash(message, 'info')

def warning(message):
    return flash(message, 'warning')
