<template>
  <div class="home">
    <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          Vue django todo app
        </a>
      </div>
    </nav>

    <hr>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form>
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input is-primary" type="text">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select is-primary">
                <select>
                  <option value="todo">To do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <hr>

   <div class="columns">
      <div class="column is-4 is-offset-1">
        <h2 class="subtitle" align="center">To do</h2>
        <div class="todo">
          <div class="card" v-for="task in tasks" v-if="task.status === 'todo'" v-bind:key="task.id">
            <div class="card-content">
              
            </div>
            <footer class="card-footer">
              <a class="card-footer-item">Done</a>
            </footer>
          </div>
        </div>
      </div>

      <div class="column is-4 is-offset-2">
        <h2 class="subtitle" align="center">Done</h2>
        <div class="done">
          <div class="card" v-for="task in tasks" v-if="task.status === 'done'" v-bind:key="task.id">
            <div class="card-content">
              
            </div>
            <footer class="card-footer">
              <a class="card-footer-item">Cancel</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'https://vue-drf-todo.herokuapp.com/api/'
const USERNAME = 'admin'
const PASSWORD = '1234'

export default {
  name: 'Home',
  created() {
    document.title = 'Vue-Django TODO App';
  },
  data() {
    return {
      tasks: [],
      description: '',
      status: 'todo'
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks() {
      axios({
        method: 'get',
        url: API_URL + 'tasks/',
        auth: {
          username: USERNAME,
          password: PASSWORD
        }
      }).then(response => this.tasks = response.data)
    }
  }
}
</script>

<style lang="scss">
.select, select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}
</style>