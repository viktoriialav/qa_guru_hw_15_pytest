## github.com в мобильном и десктопном варианте

- Реализовать автотест для **github.com**, который заходит на страницу, ищет кнопку **Sign up**, и тыкает на нее (авторизоваться не нужно)
- Параметризовать тест различным размером окна браузера.
- Сделать три варианта пропуска неподходящих параметров и тестов:
  1. Пропустить мобильный тест, если соотношение сторон десктопное (и наоборот)
  2. Переопределить параметр с помощью **indirect**
  3. Сделать разные фикстуры для каждого теста
