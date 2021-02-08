/*
 * @Description: Task Store
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-06 22:32:57
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-08 11:51:16
 */
import axios from 'axios'

const API_URL = 'http://localhost:8000'

export const state = () => ({
  tasks: [],
})

export const actions = {
  async getAllTasks({ commit }) {
    const { data } = await axios.get(`${API_URL}/tasks/`)
    commit('set', data)
  },
  async postNewTask({ commit }, payload) {
    const { data } = await axios.post(`${API_URL}/tasks/`, payload)
    commit('add', data)
  },
  async deleteTask({ commit }, id) {
    await axios.delete(`${API_URL}/tasks/${id}/`)
    commit('remove', id)
  },
  async updateTask({ commit }, payload) {
    const { id, task } = payload
    // patch和put的区别，patch只更新给定的内容，其余保持不变
    // put更新给定的类型，其余的则会全部用默认值
    // patch可以取代put, 同时更节省带宽
    await axios.patch(`${API_URL}/tasks/${id}/`, task)
    commit('edit', payload)
  },
}

export const mutations = {
  set(state, tasks) {
    state.tasks = tasks
  },
  add(state, task) {
    state.tasks.push(task)
  },
  edit(state, { id, task }) {
    const index = state.tasks.findIndex((task) => task.id === id)
    const updatedTask = { ...state.tasks[index], ...task }
    state.tasks.splice(index, 1, updatedTask)
  },
  remove(state, id) {
    const index = state.tasks.findIndex((task) => task.id === id)
    state.tasks.splice(index, 1)
  },
  toggle(state, todo) {
    todo.done = !todo.done
  },
}
