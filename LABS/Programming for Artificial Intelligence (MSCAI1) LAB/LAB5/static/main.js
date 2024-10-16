// main.js

document.addEventListener('DOMContentLoaded', function() {
    // Flash mesajlarını otomatik olarak gizleme
    setTimeout(function() {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            alert.style.display = 'none';
        });
    }, 5000); // 5 saniye sonra
});
