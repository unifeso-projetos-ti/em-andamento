import { addDoc, collection, doc, updateDoc } from '@firebase/firestore'
import { zodResolver } from '@hookform/resolvers/zod'
import { getLocalTimeZone } from '@internationalized/date'
import {
  Autocomplete,
  AutocompleteItem,
  Avatar,
  Button,
  Input,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalProps,
} from '@nextui-org/react'
import { IconCategory, IconCoin, IconUser } from '@tabler/icons-react'
import { useRouter } from 'next/navigation'
import { REVENUE_CATEGORIES } from 'public/constants/revenue/revenueCategory'
import { USERS } from 'public/constants/users'
import { useState } from 'react'
import { Controller, SubmitHandler, useForm } from 'react-hook-form'
import toast from 'react-hot-toast'
import DatePickerComponent from 'src/components/DatePicker/datePicker'
import { db } from 'src/lib/firebase'
import { z } from 'zod'

interface CreateRevenueModalProps extends Omit<ModalProps, 'children'> {
  id: string
  isOpen: boolean
  onClose: () => void
  onConfirm?: () => void
}

export default function CreateRevenueModal({
  id = '',
  isOpen,
  onClose,
  onConfirm,
  ...modalProps
}: CreateRevenueModalProps) {
  const [loading, setLoading] = useState(false)
  const router = useRouter()

  type CreateCostSchema = z.infer<typeof createCostSchema>

  const createCostSchema = z.object({
    costs: z.string(),
    category: z.number(),
    user: z.number(),
    date: z.custom<any>(),
  })

  const {
    register,
    handleSubmit,
    formState: { errors },
    control,
  } = useForm<CreateCostSchema>({
    resolver: zodResolver(createCostSchema),
  })

  const onSubmit: SubmitHandler<CreateCostSchema> = async (data) => {
    const formattedDate = data.date
      .toDate(getLocalTimeZone())
      .toISOString()
      .split('T')[0]

    const formatData = {
      ...data,
      date: formattedDate,
    }

    setLoading(true)

    if (!id) {
      try {
        await addDoc(collection(db, 'revenue'), formatData)
        toast.success('Receita criado com sucesso!', {
          style: {
            borderRadius: '10px',
            background: '#ffffff',
            border: `1.5px solid #000000`,
            color: '#000000',
          },
        })
        onClose()
        router.push('/revenue')
      } catch (err) {
        console.error('Error adding document: ', err)
      } finally {
        setLoading(false)
      }
    } else {
      try {
        await updateDoc(doc(db, 'revenue', id), {
          formatData,
        })
        toast.success('Receita atualizada com sucesso!', {
          style: {
            borderRadius: '10px',
            background: '#ffffff',
            border: `1.5px solid #000000`,
            color: '#000000',
          },
        })
        onClose()
        setLoading(false)
      } catch (err) {
        console.error(err)
        setLoading(false)
      }
    }
  }

  return (
    <Modal isOpen={isOpen} onClose={onClose} placement="top-center">
      <ModalContent>
        <>
          <ModalHeader className="flex flex-col gap-1">
            Adicionar ganho
          </ModalHeader>
          <form onSubmit={handleSubmit(onSubmit)}>
            <ModalBody>
              <Controller
                name="user"
                control={control}
                render={({ field, fieldState: { error } }) => (
                  <Autocomplete
                    selectedKey={String(field.value)}
                    label="Usuário(a)"
                    variant="bordered"
                    defaultItems={USERS}
                    placeholder="Pesquise pelo(a) usuário(a)"
                    errorMessage={error?.message}
                    endContent={<IconUser className="text-xl" />}
                    onSelectionChange={(key) => field.onChange(Number(key))}
                    isRequired
                    required
                    listboxProps={{
                      emptyContent: 'Resultado não encontrado',
                    }}
                  >
                    {(author) => (
                      <AutocompleteItem
                        key={author.id}
                        value={String(author.id)}
                        textValue={author.name}
                      >
                        <div className="flex gap-2 items-center">
                          <Avatar
                            alt={author.name}
                            className="flex-shrink-0"
                            size="sm"
                            src={author.profile_image}
                          />
                          <div className="flex flex-col">
                            <span className="text-small">{author.name}</span>
                            <span className="text-tiny text-default-400">
                              {author.email}
                            </span>
                          </div>
                        </div>
                      </AutocompleteItem>
                    )}
                  </Autocomplete>
                )}
              />

              <Controller
                name="category"
                control={control}
                render={({ field, fieldState: { error } }) => (
                  <Autocomplete
                    selectedKey={String(field.value)}
                    label="Categoria"
                    variant="bordered"
                    defaultItems={REVENUE_CATEGORIES}
                    placeholder="Pesquise pela categoria"
                    errorMessage={error?.message}
                    endContent={<IconCategory className="text-xl" />}
                    onSelectionChange={(key) => field.onChange(Number(key))}
                    isRequired
                    required
                    listboxProps={{
                      emptyContent: 'Resultado não encontrado',
                    }}
                  >
                    {(author) => (
                      <AutocompleteItem
                        key={author.id}
                        value={String(author.id)} // Certifique-se de que a chave seja uma string
                        textValue={author.name}
                      >
                        <div className="flex gap-2 items-center">
                          {/* <Avatar
              alt={author.name}
              className="flex-shrink-0"
              size="sm"
              src={author.icon}
            /> */}
                          <div className="flex flex-col">
                            <span className="text-small">{author.name}</span>
                          </div>
                        </div>
                      </AutocompleteItem>
                    )}
                  </Autocomplete>
                )}
              />

              <DatePickerComponent
                isRequired
                className="w-full"
                variant="bordered"
                control={control}
                name="date"
                label="Data"
              />

              <Input
                {...register('costs')}
                endContent={
                  <IconCoin className="text-2xl text-default-400 pointer-events-none flex-shrink-0" />
                }
                isRequired
                label="Gasto"
                placeholder="Adicionar gasto"
                variant="bordered"
                errorMessage
              />
              {/* <div className="flex py-2 items-center justify-between">
              <Checkbox
                {...register('is_recurrent')}
                classNames={{
                  label: 'text-sm',
                }}
              >
                Recorrente
              </Checkbox>
            </div> */}
            </ModalBody>
            <ModalFooter className="w-full items-center justify-between">
              <Button
                type="button"
                color="danger"
                variant="flat"
                onPress={onClose}
              >
                Fechar
              </Button>
              <Button
                disabled={loading}
                isLoading={loading}
                type="submit"
                color="primary"
                onPress={onConfirm}
              >
                Confirmar
              </Button>
            </ModalFooter>
          </form>
        </>
      </ModalContent>
    </Modal>
  )
}
