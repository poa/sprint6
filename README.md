# Sprint 6. Final project

* Проект содержит автотесты на базе `pytest` и `selenium` для сервиса [Yandex Scooter](https://qa-scooter.praktikum-services.ru/)

* Установить зависимости 

    ```shell
    pip install -r requirements.txt.
    ```
* Для запуска тестов использовать следующую команду
 
    ```shell
    pytest -v
    ```
  
* Для запуска тестов с формированием отчёта allure использовать следующую команду
 
    ```shell
    pytest -v --alluredir=allure-results
    ```
  
* Для просмотра отчёта allure (allure предварительно должен быть [установлен](https://allurereport.org/docs/install/)) выполнить команду:

    ```shell
    allure serve allure-results
    ```
