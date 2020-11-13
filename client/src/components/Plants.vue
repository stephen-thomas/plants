<template>
  <div>
    <navbar></navbar>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Plant</th>
                <th scope="col"># Photos</th>
                <th scope="col">Xp</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(plant, index) in plants" :key="index">
                <td>{{ plant.name }}</td>
                <td>{{ plant.numPictures }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                    type="button"
                    class="btn btn-info btn-sm"
                    v-b-modal.plant-update-modal
                    @click="focusPlant(plant)">
                    Focus
                  </button>
                </div>
              </td>
            </tr>
            <b-card class="mt-3" :header="focus.name" style="margin-bottom: 0.5em;" v-if="focus">
              <div class="col-md-8">
                <img :src="focus.picture"></img>
              </div>
            </b-card>
          </tbody>
        </table>
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
      plants: [],
      focus: null,
    };
  },
  components: {
    navbar: Navbar,
  },
  methods: {
    getPlants() {
      const path = 'http://localhost:5000/plants';
      axios.get(path)
        .then((res) => {
          this.plants = res.data.plants;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    focusPlant(plant) {
      this.focus = plant;
    },
  },
  created() {
    this.getPlants();
  },
};
</script>
