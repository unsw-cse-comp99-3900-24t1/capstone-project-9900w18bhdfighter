import { AllocationReqDTO, AllocationRspDTO } from '../types/allocation'
import api from './config'

const getAllocations = async () =>
  api.get<AllocationRspDTO[]>('api/allocations')

const approveAllocation = async () => api.post('api/allocations/approve')

const rejectAllocation = async () => api.delete('api/allocations/reject')

const createAllocation = async () => api.post('api/allocations')
const addOneAllocation = async (allocation: AllocationReqDTO) => {
  return api.post<AllocationRspDTO>('api/allocations/add', allocation)
}
const delOneAllocation = async (allocationId: number) => {
  return api.delete(`api/allocations/${allocationId}`)
}

export {
  getAllocations,
  approveAllocation,
  rejectAllocation,
  createAllocation,
  addOneAllocation,
  delOneAllocation,
}
