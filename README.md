# Dukaan Application

### Local Operations
- To run docker containers services locally
  ```shell
  $ make run
  ```

*`Commands to run when container is up and running.`*
- To project root directory (inside running container)
  ```shell
  $ make cli
  ```
- To run `shell_plus`
  ```shell
  $ make shell
  ```
- To run `makemigrations` & `migrate`
  ```shell
  $ make syncdb
  ```
