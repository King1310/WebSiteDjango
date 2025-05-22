document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('uploadBtn');
    const fileInput = document.querySelector('input[type="file"]');
    const form = document.getElementById('photoForm');
    uploadBtn.addEventListener('click', function() {
        fileInput.click();
    });
    fileInput.addEventListener('change', function() {
        form.submit();
    });
});