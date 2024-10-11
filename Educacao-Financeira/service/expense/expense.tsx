import {
  collection,
  deleteDoc,
  doc,
  getDoc,
  onSnapshot,
  query,
} from '@firebase/firestore'
import toast from 'react-hot-toast'
import { db } from 'src/lib/firebase'
import { IDataExpense, IExpense } from 'src/models/expense/expense'

export function getExpenses(
  setExpense: (expense: IDataExpense[]) => void,
  setLoading: (loading: boolean) => void,
  includeInactive: boolean = false
) {
  setLoading(true)

  const revenueQuery = includeInactive
    ? query(collection(db, 'expense'))
    : query(collection(db, 'expense')) // Adicione a lógica para incluir apenas ativos se necessário

  const unsub = onSnapshot(
    revenueQuery,
    (snapshot) => {
      const list: IDataExpense[] = snapshot.docs.map((doc) => {
        const data = doc.data()

        const expense: IExpense = {
          category: data.category,
          sub_category: data.sub_category,
          costs: data.costs,
          date: data.date,
          user: data.user,
        }

        return {
          id: doc.id,
          expense,
        }
      })

      setExpense(list)
      setLoading(false)
    },
    (error) => {
      console.error('Error fetching expense:', error)
      setLoading(false)
    }
  )

  return () => unsub()
}

export async function getExpenseById(
  expenseId: string,
  setExpense: (expense: IDataExpense) => void,
  setLoading: (loading: boolean) => void
) {
  try {
    setLoading(true) // Define o estado de carregamento como verdadeiro

    const docRef = doc(db, 'expense', expenseId)
    const snapshot = await getDoc(docRef)

    if (snapshot.exists()) {
      const revenueData = snapshot.data() as IDataExpense

      setExpense(revenueData)
    } else {
      console.error('No expense found for the given expenseId')
    }
  } catch (error) {
    console.error('Error fetching expense by id:', error)
  } finally {
    setLoading(false) // Finaliza o carregamento
  }
}

export const deleteExpense = async (
  id: string,
  setLoading: (loading: boolean) => void
) => {
  if (!id) return
  setLoading(true)
  try {
    await deleteDoc(doc(db, 'expense', id))
    toast.success('Despesa excluída com sucesso!', {
      style: {
        borderRadius: '10px',
        background: '#ffffff',
        border: `1.5px solid #000000`,
        color: '#000000',
      },
    })
  } catch (err) {
    console.error(err)
    toast.error('Erro ao excluir a despesa, tente novamente mais tarde', {
      style: {
        borderRadius: '10px',
        background: '#ffffff',
        border: `1.5px solid #000000`,
        color: '#000000',
      },
    })
  } finally {
    setLoading(false)
  }
}
