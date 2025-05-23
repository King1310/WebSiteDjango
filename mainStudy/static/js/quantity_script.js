document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.getElementById('quantity_input');
    const incrementButton = document.getElementById('quantity_inc_button');
    const decrementButton = document.getElementById('quantity_dec_button');

    incrementButton.addEventListener('click', function() {
        quantityInput.stepUp();  // Увеличиваем количество на 1
    });

    decrementButton.addEventListener('click', function() {
        if (quantityInput.value > 1) {
            quantityInput.stepDown();  // Уменьшаем количество на 1, если больше 1
        }
    });
});
