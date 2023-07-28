# [Redemet](https://ajuda.decea.mil.br/base-de-conhecimento/api-redemet-o-que-e/)

A API key deve ser usada dessas maneiras. Em ordem de precedência:


HTTP Header
Passe a chave API para o headers X-Api-Key:

```bash
curl -H 'X-Api-Key: your_key' 'https://api-redemet.decea.gov.br/{url}'
```

GET Query Param
Passe a API Key para o parâmetro da string de consulta api_key GET:

```bash
curl 'https://api-redemet.decea.gov.br?api_key='your_key
```