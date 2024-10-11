'use client'

import { zodResolver } from '@hookform/resolvers/zod'
import { Button, Input, useDisclosure } from '@nextui-org/react'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import ConfirmModal from 'src/components/modals'
import { z } from 'zod'

// Define validation schemas
const validationSchema = z.object({
  autocomplete: z.number(), // Adjust as needed
})

const validationSchemaConfirmDialog = z.object({
  title: z.string(),
  message: z.string(),
  confirm: z.string(),
  close: z.string(),
})

// Define types based on schemas
type FormData = z.infer<typeof validationSchema>
type FormDataDialog = z.infer<typeof validationSchemaConfirmDialog>

export default function Home() {
  const [formValues, setFormValues] = useState<FormDataDialog | null>(null)
  const animals = [
    { id: 1, name: 'Cachorro', breed: 'Golden' },
    { id: 2, name: 'Gato', breed: 'Libiano' },
    { id: 3, name: 'Girafa', breed: 'Libiano' },
    { id: 4, name: 'Zebra', breed: 'Libiano' },
    { id: 5, name: 'Elefante', breed: 'Libiano' },
    { id: 6, name: 'Tigre', breed: 'Libiano' },
    { id: 7, name: 'Leão', breed: 'Libiano' },
  ]

  const { isOpen, onOpen, onClose } = useDisclosure()

  // First form handler
  const {
    register: registerDialog,
    handleSubmit: handleSubmitDialog,
    formState: { errors: errorsDialog },
    setValue: setValueDialog,
  } = useForm<FormDataDialog>({
    resolver: zodResolver(validationSchemaConfirmDialog),
  })

  // Second form handler
  const {
    register: registerAutocomplete,
    handleSubmit: handleSubmitAutocomplete,
    formState: { errors: errorsAutocomplete },
    setValue: setValueAutocomplete,
  } = useForm<FormData>({
    resolver: zodResolver(validationSchema),
  })

  const handleConfirm = () => {
    console.log('Botão de confirmação clicado!')
    // Add logic for confirmation button
  }

  const handleAutoCompleteChange = (selectedValue: any) => {
    setValueAutocomplete('autocomplete', selectedValue)
  }

  // Handle form submission to open modal with form values
  const onSubmitDialog = (data: FormDataDialog) => {
    setFormValues(data)
    onOpen()
  }

  return (
    <main className="p-4 h-full ">
      <header className="flex justify-center">
        <h1 className="text-2xl font-bold">Apresentação do Boilerplate</h1>
      </header>
      <div className="w-full flex flex-col gap-16">
        <div className="w-full flex-col items-center justify-center">
          <h1 className="font-bold">Construído com Tailwind CSS</h1>

          <div className="flex flex-wrap  gap-12 mt-8">
            <div className="flex flex-col w-full max-w-[400px] gap-2">
              <h3 className="text-lg font-semibold">Abordagem Utility-first</h3>
              <p className="text-muted-foreground">
                O Tailwind oferece um conjunto de classes utilitárias
                pré-definidas que você pode usar para estilizar seus
                componentes, permitindo que você crie designs personalizados sem
                precisar escrever CSS.
              </p>
            </div>
            <div className="flex flex-col w-full max-w-[400px] gap-2">
              <h3 className="text-lg font-semibold">Design Responsivo</h3>
              <p className="text-muted-foreground">
                As capacidades de design responsivo do Tailwind facilitam a
                criação de layouts que se adaptam a diferentes tamanhos de tela,
                garantindo que sua aplicação fique ótima em qualquer
                dispositivo.
              </p>
            </div>
            <div className="flex flex-col w-full max-w-[400px] gap-2">
              <h3 className="text-lg font-semibold">Personalização Fácil</h3>
              <p className="text-muted-foreground">
                O sistema de design do Tailwind é altamente personalizável,
                permitindo que você mude facilmente cores, tipografia e outros
                elementos de design para combinar com a identidade da sua marca.
              </p>
            </div>
            <div className="flex flex-col w-full max-w-[400px] gap-2">
              <h3 className="text-lg font-semibold">Foco em Performance</h3>
              <p className="text-muted-foreground">
                O Tailwind é projetado com foco em performance, gerando apenas o
                CSS que é usado em sua aplicação, resultando em tamanhos de
                bundle menores e tempos de carregamento mais rápidos.
              </p>
            </div>
            <div className="flex flex-col w-full max-w-[400px] gap-2">
              <h3 className="text-lg font-semibold">
                Produtividade do Desenvolvedor
              </h3>
              <p className="text-muted-foreground">
                Ao fornecer um conjunto abrangente de classes utilitárias, o
                Tailwind ajuda os desenvolvedores a trabalhar de forma mais
                eficiente, reduzindo o tempo gasto escrevendo e mantendo CSS
                personalizado.
              </p>
            </div>
            <div className="flex flex-col w-full max-w-[400px] gap-2">
              <h3 className="text-lg font-semibold">Design Consistente</h3>
              <p className="text-muted-foreground">
                A abordagem utility-first do Tailwind incentiva um sistema de
                design consistente, garantindo que sua aplicação tenha uma
                aparência e sensação coesas e visualmente atraentes.
              </p>
            </div>
          </div>
        </div>

        <div className="w-full flex-col items-center justify-center">
          <h1 className="font-bold">Modal de confirmação personalizado</h1>

          <form
            onSubmit={handleSubmitDialog(onSubmitDialog)}
            className="flex flex-col gap-4 mt-4"
          >
            <div className="flex gap-4">
              <Input
                {...registerDialog('title')}
                errorMessage={errorsDialog.title?.message}
                type="text"
                variant="flat"
                label="Título"
              />
              <Input
                {...registerDialog('message')}
                errorMessage={errorsDialog.message?.message}
                type="text"
                variant="flat"
                label="Mensagem"
              />
            </div>
            <div className="flex gap-4">
              <Input
                {...registerDialog('close')}
                errorMessage={errorsDialog.close?.message}
                type="text"
                variant="flat"
                label="Texto botão negar"
              />
              <Input
                {...registerDialog('confirm')}
                errorMessage={errorsDialog.confirm?.message}
                type="text"
                variant="flat"
                label="Texto botão aceitar"
              />
            </div>

            <Button
              color="secondary"
              variant="shadow"
              type="submit"
              className="w-fit"
            >
              Modal de confirmação
            </Button>
          </form>

          <ConfirmModal
            size="lg"
            isOpen={isOpen}
            onClose={onClose}
            onConfirm={handleConfirm}
            message={formValues?.message || ''}
            title={formValues?.title || ''}
            confirm={formValues?.confirm || ''}
            close={formValues?.close || ''}
          />
        </div>
      </div>
    </main>
  )
}
