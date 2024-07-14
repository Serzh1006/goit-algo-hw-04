# “Алгоритми сортування”

Встановлення віртуального середовища:

------for windows------

1. Встановлення

python -m venv myenv

2. Активація

myenv\Scripts\activate

3. Деактивація

deactivate

------for macOS and linux------

1. Встановлення

python3 -m venv myenv

2. Активація

source myenv/bin/activate

3. Деактивація

deactivate

Далі потрібно встановити пакет 'prettytable', при цьому потрібно знаходитись у віртуальному середовищі, щоб пакет був встановлений тільки на цьому проєкті.

pip install prettytable

#Висновки після тестування
Вбудовані функції sort і sorted: - Вбудована функція sort (яка викликається на списках) і функція sorted (яка повертає новий відсортований список) є найшвидшими методами сортування. Це тому, що вони використовують високоефективний алгоритм Timsort, який має складність O(n log n) у найгіршому випадку. Timsort спеціально розроблений для використання в реальних додатках і поєднує в собі переваги сортування злиттям і сортування вставками, що робить його надзвичайно швидким для більшості реальних даних.

Метод вставки: - Алгоритм сортування вставками має часову складність O(n^2) у найгіршому випадку, що робить його менш ефективним для великих списків порівняно з Timsort. Цей метод працює шляхом послідовного перебору елементів і вставки кожного елемента в його правильне місце серед уже відсортованих елементів. Він працює швидше на невеликих масивах або майже відсортованих масивах.
Метод злиття: - Алгоритм сортування злиттям має часову складність O(n log n) як у найгіршому, так і в середньому випадку, що робить його теоретично таким же ефективним, як і Timsort. Однак, сортування злиттям може займати більше часу на практиці через додаткові накладні витрати на створення допоміжних масивів і складність реалізації. Це може пояснити, чому у вашому випадку сортування злиттям зайняло більше часу.

![screen table](/result_sort.png)

На таблиці видно, що метод sort трішки швидше за sorted. Це тому, що sorted робить копію масиву та повертає його не змінюючи оригінал. Метод злиттям теж є ефективним методом сортування навіть для великих даних. А от метод вставки показав себе дуже повільним на великому масиві і тому його не бажано використовувати для даних більше 1000 елементів.
