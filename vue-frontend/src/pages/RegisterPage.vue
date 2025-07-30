<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="handleRegister">
        <input v-model="username" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button type="submit">Register</button>
        <p v-if="message">{{ message }}</p>
        </form>
    </div>
    </template>

    <script>
    import { register } from '@/auth/register';

    export default {

    data() {
        return {
        username: '',
        password: '',
        message: '',
        };
    },

    methods: {
        async handleRegister() {
        const result = await register(this.username, this.password);
        this.message = result.message;

        if (result.success) {
            this.$router.push('/login');
        }
        },
    },
};
</script>
<style scoped>
div {
  max-width: 400px;
  margin: 100px auto;
  padding: 2rem;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  transition: border-color 0.2s;
}

input:focus {
  outline: none;
  border-color: #007bff;
}

button {
  padding: 0.75rem;
  background-color: #007bff;
  color: white;
  font-size: 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0056b3;
}

p {
  text-align: center;
  color: #d9534f; /* red for errors */
  font-weight: bold;
}
</style>

