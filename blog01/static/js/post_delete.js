document.addEventListener('DOMContentLoaded', function() {
    function showDeletePopup(pk) {
        const deletePopup = document.getElementById('deletePopup');
        const deleteForm = document.getElementById('deleteForm');

        deletePopup.style.display = 'flex';
    }

    function hideDeletePopup() {
        const deletePopup = document.getElementById('deletePopup');
        deletePopup.style.display = 'none';
    }

    window.showDeletePopup = showDeletePopup;
    window.hideDeletePopup = hideDeletePopup;
});
