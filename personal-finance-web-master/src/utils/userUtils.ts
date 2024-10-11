import { USERS } from 'public/constants/users'
import { IUser } from 'src/models/user'

export const getUserById = (userId: number): IUser | undefined => {
  return USERS.find((user) => user.id === userId)
}
