<template>
  <div>
    <navbar></navbar>
    <div class="container">
      <div class="row">
        {{this.user}}
      </div>
    </div>
  </div>

</div>
</template>

<script>
import axios from 'axios';
import Navbar from './Navbar.vue'

export default {
  data() {
    return {
      user: null,
    };
  },
  components: {
    navbar: Navbar,
  },
  methods: {
    getUserData() {
      const path = 'http://localhost:5000/user';
      axios.get(path)
        .then((res) => {
          this.user = res.data.user;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getUserData();
  },
};
</script>
