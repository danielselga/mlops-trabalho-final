<template>
  <v-container>
      <v-form @submit.prevent>
        <v-row>
          <v-col>
            <v-text-field
              v-model="firstName"
              :rules="rules"
              label="First name"
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="firstName"
              :rules="rules"
              label="First name"
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="firstName"
              :rules="rules"
              label="First name"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-btn type="submit" @click="test" block class="mt-2">Submit</v-btn>
      </v-form>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    firstName: "",
    rules: [
      (value) => {
        if (value) return true;
        return "You must enter a first name.";
      },
    ],
  }),
  methods: {
    test() {
      console.log("submit 1");
    },
  },
};
</script>
