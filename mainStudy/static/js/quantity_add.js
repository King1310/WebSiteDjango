document.addEventListener('DOMContentLoaded', function() {
    function changeQuantity(itemId, change) {
        const quantityInput = document.getElementById('quantity-' + itemId);
        let currentQuantity = parseInt(quantityInput.value);

        // Изменяем количество, добавляя или убирая 1
        let newQuantity = currentQuantity + change;

        // Проверка на минимальное значение
        if (newQuantity >= 1) {
            quantityInput.value = newQuantity;
        }
    }

    // Получаем все кнопки увеличения и уменьшения
    const incButtons = document.querySelectorAll('.quantity_inc');
    const decButtons = document.querySelectorAll('.quantity_dec');

    // Добавляем обработчики событий для кнопок увеличения
    incButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            changeQuantity(itemId, 1); // Увеличиваем количество на 1
        });
    });

    // Добавляем обработчики событий для кнопок уменьшения
    decButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            changeQuantity(itemId, -1); // Уменьшаем количество на 1
        });
    });
});
