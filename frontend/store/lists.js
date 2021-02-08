/*
 * @Description: List Store
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-08 14:08:47
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-08 15:28:01
 */
import axios from 'axios'

const API_URL = 'http://localhost:8000'

export const state = {
  lists: [],
}

export const actions = {
  async getAllLists({ commit }) {
    const { data } = await axios.get(`${API_URL}/lists/`)
    commit('set', data)
  },
  async postNewList({ commit }, payload) {
    const { data } = await axios.post(`${API_URL}/lists/`, payload)
    commit('add', data)
  },
  async deleteList({ commit }, id) {
    await axios.delete(`${API_URL}/lists/${id}/`)
    commit('remove', id)
  },
  async updateList({ commit }, payload) {
    const { id, list } = payload
    // patch和put的区别，patch只更新给定的内容，其余保持不变
    // put更新给定的类型，其余的则会全部用默认值
    // patch可以取代put, 同时更节省带宽
    await axios.patch(`${API_URL}/lists/${id}/`, list)
    commit('edit', payload)
  },
}

export const mutations = {
  set(state, lists) {
    state.lists = lists
  },
  add(state, list) {
    state.lists.push(list)
  },
  remove(state, id) {
    const index = state.lists.findIndex((list) => list.id === id)
    state.lists.splice(index, 1)
  },
  edit(state, { id, list }) {
    const index = state.lists.findIndex((list) => list.id === id)
    const updatedList = { ...state.lists[index], ...list }
    state.lists.splice(index, 1, updatedList)
  },
}
