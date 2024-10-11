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
import { IDataRevenue, IRevenue } from 'src/models/revenue'

export function getRevenues(
  setRevenue: (revenue: IDataRevenue[]) => void,
  setLoading: (loading: boolean) => void,
  includeInactive: boolean = false
) {
  setLoading(true)

  // Verifica se inclui ou não registros inativos
  const revenueQuery = includeInactive
    ? query(collection(db, 'revenue'))
    : query(collection(db, 'revenue')) // Adicione a lógica para incluir apenas ativos se necessário

  const unsub = onSnapshot(
    revenueQuery,
    (snapshot) => {
      const list: IDataRevenue[] = snapshot.docs.map((doc) => {
        const data = doc.data()

        const revenue: IRevenue = {
          category: data.category,
          costs: data.costs,
          date: data.date,
          user: data.user,
        }

        return {
          id: doc.id,
          revenue,
        }
      })

      setRevenue(list)
      setLoading(false)
    },
    (error) => {
      console.error('Error fetching revenue:', error)
      setLoading(false)
    }
  )

  return () => unsub()
}

export async function getRevenueById(
  revenueId: string,
  setRevenue: (revenue: IDataRevenue) => void,
  setLoading: (loading: boolean) => void
) {
  try {
    setLoading(true) // Define o estado de carregamento como verdadeiro

    const docRef = doc(db, 'revenue', revenueId)
    const snapshot = await getDoc(docRef)

    if (snapshot.exists()) {
      const revenueData = snapshot.data() as IDataRevenue

      setRevenue(revenueData)
    } else {
      console.error('No revenue found for the given revenueId')
    }
  } catch (error) {
    console.error('Error fetching revenue by id:', error)
  } finally {
    setLoading(false) // Finaliza o carregamento
  }
}

export const deleteRevenue = async (
  id: string,
  setLoading: (loading: boolean) => void
) => {
  if (!id) return
  setLoading(true)
  try {
    await deleteDoc(doc(db, 'revenue', id))
    toast.success('Receita excluída com sucesso!', {
      style: {
        borderRadius: '10px',
        background: '#ffffff',
        border: `1.5px solid #000000`,
        color: '#000000',
      },
    })
  } catch (err) {
    console.error(err)
    toast.error('Erro ao excluir a receita, tente novamente mais tarde', {
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
