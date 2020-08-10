# How to pull environment variables with Helm Charts

## Need
- Argo Workflow Container의 env 에서 여러개의 환경변수를 range 를 이용하여 넣고 싶었음
- https://stackoverflow.com/questions/49928819/how-to-pull-environment-variables-with-helm-charts

### 해결(2020-08-10)
```yaml
container:
  image: blahblah:cslee-0.0.1
  env:
    {{- range $key, value := .Values.blah.correct }}
    - name: {{ $key }}
      value: {{ $value }}
    {{end -}}
```

### Error Log
- ReadString: expects \" or n, but found
- https://github.com/argoproj/argo/issues/632
