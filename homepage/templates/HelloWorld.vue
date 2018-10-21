<template>

  <div class="hello">



  Welcome to Developers

    <h1>Hi!</h1>

    <form>

        <p>

          <label>User ID</label>

          <input type = "text"

                  v-model="username"

                 id = "username" />

        </p>

        <p>

          <label>Password</label>

          <input type = "password"

                  v-model="password"

                 id = "password" />

        </p>

        <button @click=authenticate>Login</button>

    </form>



  </div>

</template>



<script>

export default {

  name: 'HelloWorld',

  data () {

    return {

      msg: 'Welcome to Your Vue.js App',

      username: '',

      password: ''

    }

  },

  methods: {

    authenticate () {

      if (this.username === 'user' && this.password === 'pwd') {

        this.$router.push({ path: '/home' })

      } else { alert('Wrong Password') }

    }

  }

}

</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>

h1, h2 {

  font-weight: normal;

}

ul {

  list-style-type: none;

  padding: 0;

}

li {

  display: inline-block;

  margin: 0 10px;

}

a {

  color: #42b983;

}

</style>